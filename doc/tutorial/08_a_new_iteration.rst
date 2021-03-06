Defining a New Iteration
------------------------

LASIF organizes the actual inversion in an arbitrary number of iterations; each
of which is described by a single XML file. Within each file, the events and
stations for this iterations, the solver settings, and other information is
specified. Each iteration can have an arbitrary name. It is probably a good
idea to give simple numeric names, like 1, 2, 3, ...

Let's start by creating the XML file for the first iteration with the
**create_new_iteration** command.

.. code-block:: bash

    $ lasif create_new_iteration 1 40.0 100.0 SES3D_4_1


This command takes four arguments; the first being the iteration name. A simple
number is sufficient in many cases. The second and third denote the band limit
of this iteration. In this example the band is limited between 40 and 100
seconds. The fourth argument is the waveform solver to be used for this
iteration. It currently only supports SES3D 4.1 but the infrastructure to add
other solvers is already in place.

You will see that this create a new file: ``ITERATIONS/ITERATION_1.xml``.
Each iteration will have its own file. To get a list of iterations, use

.. code-block:: bash

    $ lasif list_iterations

    1 Iteration in project:
    1


To get more information about a specific iteration,  use the ``iteration_info``
command.

.. code-block:: bash

    $ lasif iteration_info 1

    LASIF Iteration
    Name: 1
    Description: None
    Source Time Function: Filtered Heaviside
    Preprocessing Settings:
        Highpass Period: 100.000 s
        Lowpass Period: 40.000 s
    Solver: SES3D 4.1 | 500 timesteps (dt: 0.75s)
    2 events recorded at 51 unique stations
    102 event-station pairs ("rays")

.. note::

    You might have noticed the pairs of **list_x** and **x_info** commands, e.g.
    **list_events** and **event_info** or **list_iterations** and
    **iteration_info**. This scheme is true for most things in LASIF. The
    **list_x** variant is always used to get a quick overview of everything
    currently part of the LASIF project. The **x_info** counterpart returns
    more detailed information about the resource.

The Iteration XML Files
^^^^^^^^^^^^^^^^^^^^^^^

The XML file defining each iteration attempts to be a collection of all
information relevant for a single iteration.

.. note::

    The iteration XML files are the **main provenance information** (in
    combination with the log files) within LASIF. By keeping track of what
    happened during each iteration it is possible to reasonably judge how any
    model came into being.


If at any point you feel the need to keep track of additional information
and there is no place for it within LASIF, please contact the developers.
LASIF aims to offer an environment where all necessary information can be
stored in an organized and sane manner.


The iteration XML files currently contain:

* Some metadata: the iteration name, a description and some comments.
* A limited data preprocessing configuration. The data preprocessing is
  currently mostly fixed and only the desired frequency content can be chosen.
  Keep in mind that these values will also be used to filter the source time
  function.
* Some data rejection criterias. This will be covered in more detail later on.
* The source time function configuration.
* The settings for the solver used for this iteration.
* A list of all events used for the iteration. Here it is possible to apply
  weights to the different events and also to apply a time correction. It can
  differ per iteration.
* Each event contains a list of stations where data is available. Furthermore
  each station can have a different weight and time correction.

This file is rather verbose but also very flexible. It is usually only
necessary to create this file once and then make a copy and small adjustments
for each iteration. In the future some more user-friendly ways to deal with the
information will hopefully be incorporated into LASIF.


Let's have a quick look at the generated file. The **create_new_iteration**
command will create a new iteration file with all the information currently
present in the LASIF project.

.. code-block:: xml

    <?xml version='1.0' encoding='UTF-8'?>
    <iteration>
      <iteration_name>1</iteration_name>
      <data_preprocessing>
        <highpass_period>100.0</highpass_period>
        <lowpass_period>40.0</lowpass_period>
      </data_preprocessing>
      <rejection_criteria>...</rejection_criteria>
      <solver_parameters>
        <solver>SES3D 4.1</solver>
        <solver_settings>
          <simulation_parameters>
            <number_of_time_steps>2000</number_of_time_steps>
            <time_increment>0.3</time_increment>
            <is_dissipative>false</is_dissipative>
          </simulation_parameters>
          <output_directory>../OUTPUT/{{EVENT_NAME}}</output_directory>
          <adjoint_output_parameters>...</adjoint_output_parameters>
          <computational_setup>
            <nx_global>24</nx_global>
            <ny_global>24</ny_global>
            <nz_global>15</nz_global>
            <lagrange_polynomial_degree>4</lagrange_polynomial_degree>
            <px_processors_in_theta_direction>2</px_processors_in_theta_direction>
            <py_processors_in_phi_direction>2</py_processors_in_phi_direction>
            <pz_processors_in_r_direction>1</pz_processors_in_r_direction>
          </computational_setup>
          <relaxation_parameter_list>
            ...
          </relaxation_parameter_list>
        </solver_settings>
      </solver_parameters>
      <event>
        <event_name>GCMT_event_NORTHWESTERN_BALKAN_REGION_Mag_5.9_1980-5-18-20-2</event_name>
        <event_weight>1.0</event_weight>
        <time_correction_in_s>0.0</time_correction_in_s>
        <station>
          <station_id>LA.AA22</station_id>
          <station_weight>1.0</station_weight>
          <time_correction_in_s>0.0</time_correction_in_s>
        </station>
        <station>
          ...
        </station>
      </event>
        ...
      <event>
      </event>
    </iteration>


It is a rather self-explaining file; some things to look out for:

* The dataprocessing frequency limits are given periods in seconds. This is
  more in line what one would normally use.
* The source time function is just given as a string. The "Filtered Heaviside"
  is the only source time function currently supported. It will be filtered
  with the limits specified in the data preprocessing section.
* The paths in the solver settings contains an **{{EVENT_NAME}}** part. This
  part will be replaced by the actual event name. This means that the file
  does not have to be adjusted for every event.

.. note::

    The file shown here has already been adjusted for the tutorial example.
    For the tutorial we will run a simulation on 4 cores (should be suitable
    for your Desktop PC/Laptop) for 2000 timesteps with a time delta of 0.3
    seconds. Please make sure to also adjust the file. The following
    parameters are essential in almost all cases (shown here with the values
    for the tutorial):

    * ``number_of_time_steps``: ``2000``
    * ``time_increment``: ``0.3``
    * ``is_dissipative``: ``false`` (in a real world application set this to ``true``)
    * ``nx_global``: ``24``
    * ``ny_global``: ``24``
    * ``nz_global``: ``15``
    * ``px_processors_in_theta_direction``: ``2``
    * ``py_processors_in_phi_direction``: ``2``
    * ``pz_processors_in_r_direction``: ``1``

    Please refer to the SES3D documentation for more information.


Source Time Functions
^^^^^^^^^^^^^^^^^^^^^

The source time functions will be dynamically generated from the information
specified in the iteration XML files. Currently only one type of source time
function, a filtered Heaviside function is supported. In the future, if
desired, it could also be possible to use inverted source time functions.

The source time function will always be defined for the number of time steps
and time increment you specify in the solver settings. Furthermore all source
time functions will be filtered with the same bandpass as the data.

To get a quick look of the source time function for any given iteration, use
the **plot_stf** command with the iteration name:

.. code-block:: bash

    $ lasif plot_stf 1

This command will read the corresponding iteration file and open a plot with a
time series and a time frequency representation of the source time function.

.. plot::

    import lasif.visualization
    import matplotlib.pylab as plt

    from lasif.function_templates import source_time_function
    data = source_time_function.source_time_function(2000, 0.3, 1.0 / 100.0,
                                                     1.0 / 40.0, None)
    lasif.visualization.plot_tf(data, 0.3, freqmin=1.0 / 100.0,
                                freqmax=1.0 / 40.0)


Attenuation
^^^^^^^^^^^

SES3D models attenuation with a discrete superposition of a finite number of
relaxation mechanisms. The goal is to achieve a constant Q model over the
chosen frequency range. Upon creating an iteration, LASIF will run a non-linear
optimization algorithm to find relaxation times and associated weights that
will be nearly constant over the chosen frequency domain.

At any point you can see the absorption-band model for a given iteration at a
couple of exemplary Q values with


.. code-block:: bash

    $ lasif plot_Q_model 1


The single argument is the name of the iteration.


.. plot::

    from lasif.tools import Q_discrete
    weights = [1.6264684983257656, 1.0142952434286228, 1.5007527644957979]
    relaxation_times = [0.68991741458188449, 4.1538611409236301,
                        23.537531778655516]

    Q_discrete.plot(weights, relaxation_times, f_min=1.0 / 100.0,
                    f_max=1.0 / 10.0)


The two vertical lines in each plot mark the frequency range as specified in
the iteration XML file.

It is also possible to directly generate the relaxation times and weights for
any frequency band. To generate a Q model approximately constant in a period
band from 10 seconds to 100 seconds use


.. code-block:: bash

    $ lasif calculate_constant_Q_model 10 100

    Starting to find optimal relaxation parameters.
    weights:              [1.60642, 1.0073, 1.49737]
    relaxation times:     [0.71721, 4.2330, 23.78702]
    partial derivatives:  [-1.68287755  0.78722974  5.14255026]
    cumulative rms error: 0.0163777833823


Data Preprocessing
^^^^^^^^^^^^^^^^^^

.. note::

    You do not actually need to do this for the tutorial.

Data preprocessing is an essential step if one wants to compare data and
seismograms. It serves several purposes: Restricting the frequency content of
the data to that of the synthetics - what is not simulated can not be seen in
synthetic seismograms. Remove the instrument response and convert to the same
units used for the synthetics (usually ``m/s``). Furthermore any linear  trends
and static offset are removed and some processing has to be performed so
that the data is available at the same points in time as the synthetics. The
goal of the preprocessing within LASIF is to create data that is directly
comparable to simulated data without any more processing.

The applied processing is identified via the name::

    preprocessed_hp_0.01000_lp_0.02500_npts_2000_dt_0.300000

or (in Python terms):

.. code-block:: python

    highpass = 1.0 / 100.0
    lowpass = 1.0 / 40.0
    npts = 2000
    dt = 0.3

    processing_tag = ("preprocessed_hp_{highpass:.5f}_lp_{lowpass:.5f}_"
                      "npts_{npts}_dt_{dt:5f}").format(highpass=highpass, lowpass=lowpass,
                                                       npts=npts, dt=dt)

.. note::

    You can use any processing tool you want, but you have to adhere to the
    directory structure otherwise LASIF will not be able to work with the data.
    It is furthermore important that the processed filenames are identical to
    the unprocessed ones.

If you feel that additional identifiers are needed to uniquely identify the
applied processing (in the limited setting of being useful for the here
performed full waveform inversion) please contact the LASIF developers.

You can of course also simply utilize LASIF's built-in preprocessing. Using it
is trivial, just launch the **preprocess_data** command together with the
iteration name.

.. code-block:: bash

    $ lasif preprocess_data 1

This will start a fully parallelized preprocessing for all data required for
the specified iteration. It will utilize all your machine's cores and might
take a while. If you repeat the command it will only process data not already
processed; an advantage is that you can cancel the processing at any time and
then later on just execute the command again to continue where you left off.
This usually only needs to be done every couple of iterations when you decide
to go to higher frequencies or add new data.

The preprocessed data will be put in the correct folder.

Data Rejection
^^^^^^^^^^^^^^

Coming soon...watch this space.


This concludes the initial setup for each iteration. The next steps is to
actually simulate anything and LASIF of course also assists in that regard.

