#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Functionality to deal with Iteration XML files.

:copyright:
    Lion Krischer (krischer@geophysik.uni-muenchen.de), 2013
:license:
    GNU General Public License, Version 3
    (http://www.gnu.org/copyleft/gpl.html)
"""
from lxml import etree
from lxml.builder import E
import os

from lasif.project import LASIFException


class Iteration(object):
    def __init__(self, iteration_xml_filename):
        """
        Init function takes a Iteration XML file.
        """
        if not os.path.exists(iteration_xml_filename):
            msg = "File '%s' not found." % iteration_xml_filename
            raise ValueError(msg)
        self._parse_iteration_xml(iteration_xml_filename)

    def _parse_iteration_xml(self, iteration_xml_filename):
        """
        Parses the given iteration xml file and stores the information with the
        class instance.
        """
        root = etree.parse(iteration_xml_filename).getroot()

        self.iteration_name = self._get(root, "iteration_name")
        self.description = self._get_if_available(root,
            "iteration_description")
        self.comments = [_i.text for _i in root.findall("comment") if _i.text]
        self.source_time_function = self._get(root, "source_time_function")

        self.data_preprocessing = {}
        prep = root.find("data_preprocessing")
        self.data_preprocessing["highpass_frequency"] = \
            float(self._get(prep, "highpass_frequency"))
        self.data_preprocessing["lowpass_frequency"] = \
            float(self._get(prep, "lowpass_frequency"))

        self.solver_settings = self._recursive_dict(root.find(
            "solver_parameters"))[1]

        self.events = {}
        for event in root.findall("event"):
            event_name = self._get(event, "event_name")
            self.events[event_name] = {
                "event_weight": float(self._get(event, "event_weight")),
                "time_correction_in_s": float(self._get(event,
                    "time_correction_in_s")),
                "stations": {}}
            for station in event.findall("station"):
                station_id = self._get(station, "station_id")
                comments = [_i.text
                    for _i in station.findall("comment") if _i.text]
                self.events[event_name]["stations"][station_id] = {
                    "station_weight": float(self._get(station,
                        "station_weight")),
                    "time_correction_in_s": float(self._get(station,
                        "time_correction_in_s")),
                    "comments": comments}

    def _get(self, element, node_name):
        return element.find(node_name).text

    def _get_if_available(self, element, node_name):
        item = element.find(node_name)
        if item is not None:
            return item.text
        return None

    def _recursive_dict(self, element):
        return element.tag, \
            dict(map(self._recursive_dict, element)) or element.text

    def __str__(self):
        """
        Pretty printing.
        """
        ret_str = (
            "LASIF Iteration\n"
            "\tName: {self.iteration_name}\n"
            "\tDescription: {self.description}\n"
            "{comments}"
            "\tSource Time Function: {self.source_time_function}\n"
            "\tPreprocessing Settings:\n"
            "\t\tHighpass Frequency: {hp:.3f} Hz\n"
            "\t\tLowpass Frequency: {lp:.3f} Hz\n"
            "\tSolver: {solver} | {timesteps} timesteps (dt: {dt}s)\n"
            "\t{event_count} events recorded at {station_count} "
            "unique stations\n"
            "\t{pair_count} event-station pairs (\"rays\")")

        comments = "\n".join("\tComment: %s" % comment
            for comment in self.comments)
        if comments:
            comments += "\n"

        all_stations = []
        for ev in self.events.itervalues():
            all_stations.extend(ev["stations"].iterkeys())

        return ret_str.format(self=self, comments=comments,
            hp=self.data_preprocessing["highpass_frequency"],
            lp=self.data_preprocessing["lowpass_frequency"],
            solver=self.solver_settings["solver"],
            timesteps=self.solver_settings["solver_settings"][
                "simulation_parameters"]["number_of_time_steps"],
            dt=self.solver_settings["solver_settings"][
                "simulation_parameters"]["time_increment"],
            event_count=len(self.events),
            pair_count=len(all_stations),
            station_count=len(set(all_stations)))


def create_iteration_xml_string(iteration_name, solver_name, events):
    """
    Creates a new iteration string.

    Returns a string containing the XML representation.

    :param iteration_name: The iteration name. Should start with a number.
    :param solver_name: The name of the solver to be used for this iteration.
    :param events: A dictionary. The key is the event name, and the value a
        list of station ids for this event.
    """
    solver_doc = _get_default_solver_settings(solver_name)
    if solver_name.lower() == "ses3d_4_0":
        solver_name = "SES3D 4.0"
    else:
        raise NotImplementedError

    # Loop over all events.
    events_doc = []
    # Also over all stations.
    for event_name, stations in events.iteritems():
        stations_doc = [E.station(
            E.station_id(station),
            E.station_weight("1.0"),
            E.time_correction_in_s("0.0")) for station in stations]
        events_doc.append(E.event(
            E.event_name(event_name),
            E.event_weight("1.0"),
            E.time_correction_in_s("0.0"),
            *stations_doc))

    doc = E.iteration(
        E.iteration_name(iteration_name),
        E.iteration_description(""),
        E.comment(""),
        E.data_preprocessing(
            E.highpass_frequency("0.01"),
            E.lowpass_frequency("0.5")),
        E.rejection_criteria(
            E.minimum_trace_length_in_s("500.0"),
            E.signal_to_noise(
                E.test_interval_from_origin_in_s("100.0"),
                E.max_amplitude_ratio("100.0"))),
        E.source_time_function("Filtered Heaviside"),
        E.solver_parameters(
            E.solver(solver_name),
            solver_doc),
        *events_doc)

    string_doc = etree.tostring(doc, pretty_print=True,
        xml_declaration=True, encoding="UTF-8")
    return string_doc


def _get_default_solver_settings(solver):
    """
    Helper function returning etree representation of a solver's default
    settings.
    """
    known_solvers = ["ses3d_4_0A"]
    if solver.lower() == "ses3d_4_0":
        from lasif.utils import generate_ses3d_4_0_template
        return generate_ses3d_4_0_template()
    else:
        msg = "Solver '%s' not known. Known solvers: %s" % (solver,
            ",".join(known_solvers))
        raise LASIFException(msg)