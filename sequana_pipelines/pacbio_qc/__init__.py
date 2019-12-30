import pkg_resources
try:
    version = pkg_resources.require("sequana_pacbio_qc")[0].version
except:
    version = ">=0.8.0"

