from config.experiment_config_lib import ControllerConfig
from sts.topology import MeshTopology
from sts.control_flow import Fuzzer, Interactive
from sts.input_traces.input_logger import InputLogger
from sts.simulation_state import SimulationConfig

# Work directory must be absolute path
work_directory = "/home-local/andrewor/work"
start_cmd = "./start_vms -d %s -h -r" % work_directory
get_address_cmd = "./show_vms -d %s -r" % work_directory
dummy_cmd = "sleep 1" 

# Use Floodlight as our controller
controllers = [ ControllerConfig(start_cmd, cwd="experiments/scripts/bsc", address="__address__", port=6633, controller_type="bsc", label="c1", get_address_cmd=get_address_cmd), 
                ControllerConfig(dummy_cmd, cwd="experiments/scripts/bsc", address="__address__", port=6633, controller_type="bsc", label="c2", get_address_cmd=get_address_cmd)]
topology_class = MeshTopology
topology_params = "num_switches=3"

simulation_config = SimulationConfig(controller_configs=controllers,
                                     topology_class=topology_class,
                                     topology_params=topology_params,
                                     kill_controllers_on_exit=False
                                     )

control_flow = Fuzzer(simulation_config,
                      check_interval=5,
                      halt_on_violation=True,
                      input_logger=InputLogger(),
                      invariant_check_name="check_everything",
                      steps=500,
                      fuzzer_params="experiments/config/fuzzer_params_heavy_failures.py"
                      )