import easydev
import os
import tempfile
import subprocess
import sys
from sequana.pipelines_common import get_pipeline_location as getpath

sharedir = getpath('pacbio_qc')


def test_standalone_subprocess():
    directory = tempfile.TemporaryDirectory()
    cmd = """sequana_pipelines_pacbio_qc --input-directory {} 
            --working-directory {} --force""".format(sharedir, directory.name)
    subprocess.call(cmd.split())


def test_standalone_script():
    directory = tempfile.TemporaryDirectory()
    import sequana_pipelines.pacbio_qc.main as m
    sys.argv = ["test", "--input-directory", sharedir, 
            "--working-directory", directory.name, "--force"]
    m.main()

def test_full1():
    with tempfile.TemporaryDirectory() as directory:
        print(directory)
        wk = directory
        cmd = "sequana_pipelines_pacbio_qc --input-directory {} "
        cmd += "--working-directory {}  --force --skip-kraken"
        cmd = cmd.format(sharedir, wk)
        subprocess.call(cmd.split())

        stat = subprocess.call("sh pacbio_qc.sh".split(), cwd=wk)

        assert os.path.exists(wk + "/multiqc_report.html")

def test_full2():
    with tempfile.TemporaryDirectory() as directory:
        print(directory)
        wk = directory
        database="~/.config/sequana/toydb"
        cmd = "sequana_pipelines_pacbio_qc --input-directory {} "
        cmd += "--working-directory {}  --force --kraken-databases {}"
        cmd = cmd.format(sharedir, wk, database)
        subprocess.call(cmd.split())

        stat = subprocess.call("sh pacbio_qc.sh".split(), cwd=wk)
        assert os.path.exists(wk + "/multiqc_report.html")

def test_version():
    cmd = "sequana_pipelines_pacbio_qc --version"
    subprocess.call(cmd.split())

