

.. image:: https://badge.fury.io/py/sequana-pacbio-qc.svg
     :target: https://pypi.python.org/pypi/sequana_pacbio_qc

.. image:: http://joss.theoj.org/papers/10.21105/joss.00352/status.svg
    :target: http://joss.theoj.org/papers/10.21105/joss.00352
    :alt: JOSS (journal of open source software) DOI


This is is the **pacbio_qc** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ projet

:Overview: Quality control for pacbio BAM files (raw data or CCS files)
:Input: BAM files provided by Pacbio Sequencers
:Output: HTML reports with various plots including taxonomic plot
:Status: production
:Citation: Cokelaer et al, (2017), ‘Sequana’: a Set of Snakemake NGS pipelines, Journal of Open Source Software, 2(16), 352, JOSS DOI doi:10.21105/joss.00352


Installation
~~~~~~~~~~~~

You must install Sequana first::

    pip install sequana

Then, just install this package::

    pip install sequana_pacbio_qc


Usage
~~~~~

::

    sequana_pipelines_pacbio_qc --help
    sequana_pipelines_pacbio_qc --input-directory DATAPATH


iIf you want to filter out some BAM files, you may use the pattern in tab 'input data'.

In the configuration tab, in the kraken section add as many databases
as you wish. You may simply unset the first database to skip the taxonomy, which
is experimental.


This creates a directory with the pipeline and configuration file. You will then need
to execute the pipeline::

    cd pacbio_qc
    sh pacbio_qc.sh  # for a local run

This launch a snakemake pipeline. If you are familiar with snakemake, you can 
retrieve the pipeline itself and its configuration files and then execute the pipeline yourself with specific parameters::

    snakemake -s pacbio_qc.rules -c config.yaml --cores 4 --stats stats.txt

Or use `sequanix <https://sequana.readthedocs.io/en/master/sequanix.html>`_ interface.

Requirements
~~~~~~~~~~~~

This pipelines requires the following executable(s):

- sequana
- kraken2
- multiqc

.. image:: https://raw.githubusercontent.com/sequana/sequana_pacbio_qc/master/sequana_pipelines/pacbio_qc/dag.png


Details
~~~~~~~~~

This pipeline takes as inputs a set of BAM files from Pacbio sequencers. It
computes a set of basic statistics related to the read lengths. It also shows
some histograms related to the GC content, SNR of the diodes and the so-called ZMW
values. Finally, a quick taxonomy can be performed using Kraken. HTML reports
are created for each sample as well as a multiqc summary page.

Kraken databases are not provided with the pipeline. This step is optional and
not used by default. 


Changelog
~~~~~~~~~
========= ====================================================================
Version   Description
========= ====================================================================
0.9.0     First release of sequana_pacbio_qc using latest sequana rules and
          modules (0.9.5)
========= ====================================================================


Contribute & Code of Conduct
~~~~~~~~~~~~~~~~~~~~~~~~~~~~

To contribute to this project, please take a look at the 
`Contributing Guidelines <https://github.com/sequana/sequana/blob/master/CONTRIBUTING.rst>`_ first. Please note that this project is released with a 
`Code of Conduct <https://github.com/sequana/sequana/blob/master/CONDUCT.md>`_. By contributing to this project, you agree to abide by its terms.


Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the `latest documented configuration file <https://raw.githubusercontent.com/sequana/sequana_pacbio_qc/master/sequana_pipelines/pacbio_qc/config.yaml>`_
to be used with the pipeline. Each rule used in the pipeline may have a section in the configuration file. 

Notes for developers
~~~~~~~~~~~~~~~~~~~~
bam_to_fasta
^^^^^^^^^^^^

.. snakemakerule:: bam_to_fasta

pacbio_quality
^^^^^^^^^^^^^^^^^^^^
.. snakemakerule:: pacbio_quality
