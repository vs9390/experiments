
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import Replayer
from sts.simulation_state import SimulationConfig
from sts.input_traces.input_logger import InputLogger

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./start_vms -d /home-local/andrewor/work -h -r', label='c1', address='10.192.5.226', cwd='experiments/scripts/bsc', controller_type='bsc'), ControllerConfig(start_cmd='sleep 1', label='c2', address='10.192.5.227', cwd='experiments/scripts/bsc', controller_type='bsc')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=False,
                 kill_controllers_on_exit=False)

control_flow = Replayer(simulation_config, "experiments/bigswitch_5_mcs/interreplay_3_l_0/events.trace",
                        input_logger=InputLogger(),
                        wait_on_deterministic_values=False,
                        allow_unexpected_messages=False,
                        pass_through_whitelisted_messages=True)
# Invariant check: 'None'