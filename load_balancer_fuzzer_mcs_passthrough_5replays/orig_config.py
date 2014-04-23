
from config.experiment_config_lib import ControllerConfig
from sts.topology import *
from sts.control_flow import EfficientMCSFinder
from sts.invariant_checker import InvariantChecker
from sts.simulation_state import SimulationConfig

simulation_config = SimulationConfig(controller_configs=[ControllerConfig(start_cmd='./pox.py --verbose --unthreaded-sh misc.ip_loadbalancer --ip=10.1.3.2 --servers=10.1.3.2,10.2.3.2 sts.util.socket_mux.pox_monkeypatcher   openflow.discovery openflow.of_01 --address=__address__ --port=__port__', label='c1', address='127.0.0.1', cwd='dart_pox')],
                 topology_class=MeshTopology,
                 topology_params="num_switches=3",
                 patch_panel_class=BufferedPatchPanel,
                 multiplex_sockets=True,
                 kill_controllers_on_exit=True)

control_flow = EfficientMCSFinder(simulation_config, "experiments/load_balancer_fuzzer/events.trace",
                                  wait_on_deterministic_values=False,
                                  delay_flow_mods=False,
                                  max_replays_per_subsequence=5,
                                  default_dp_permit=True,
                                  pass_through_whitelisted_messages=True,
                                  invariant_check_name='check_for_ofp_error',
                                  bug_signature="")
