This is is the **pacbio_qc** pipeline from the `Sequana <https://sequana.readthedocs.org>`_ projet

:Overview: QC on pacbio BAM files
:Input: BAM files provided by Pacbio Sequencers
:Output: HTML reports with various plots including taxonomic plot
:Status: draft
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

- kraken
- multiqc

.. image:: https://raw.githubusercontent.com/sequana/sequana_pacbio_qc/master/sequana_pipelines/pacbio_qc/dag.png


Details
~~~~~~~~~

This pipeline runs **pacbio_qc** in parallel on the input BAM files. 
A brief sequana summary report is also produced.


Rules and configuration details
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Here is the `latest documented configuration file <https://raw.githubusercontent.com/sequana/sequana_pacbio_qc/master/sequana_pipelines/pacbio_qc/config.yaml>`_
to be used with the pipeline. Each rule used in the pipeline may have a section in the configuration file. 

