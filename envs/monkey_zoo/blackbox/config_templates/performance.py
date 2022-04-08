from envs.monkey_zoo.blackbox.config_templates.config_template import ConfigTemplate


class Performance(ConfigTemplate):
    config_values = {
        "basic.credentials.exploit_password_list": [
            "Xk8VDTsC",
            "^NgDvY59~8",
            "Ivrrw5zEzs",
            "3Q=(Ge(+&w]*",
            "`))jU7L(w}",
            "t67TC5ZDmz",
        ],
        "basic.credentials.exploit_user_list": ["m0nk3y"],
        "basic.exploiters.exploiter_classes": [
            "SmbExploiter",
            "WmiExploiter",
            "SSHExploiter",
            "WebLogicExploiter",
            "HadoopExploiter",
            "MSSQLExploiter",
            "PowerShellExploiter",
            "ZerologonExploiter",
            "Log4ShellExploiter",
        ],
        "basic_network.network_analysis.inaccessible_subnets": [
            "10.2.2.0/30",
            "10.2.2.8/30",
            "10.2.2.21/32",
            "10.2.2.19/32",
            "10.2.2.18/32",
            "10.2.2.17/32",
        ],
        "basic_network.scope.subnet_scan_list": [
            "10.2.2.2",
            "10.2.2.3",
            "10.2.2.4",
            "10.2.2.5",
            "10.2.2.8",
            "10.2.2.9",
            "10.2.1.10",
            "10.2.0.11",
            "10.2.0.12",
            "10.2.2.11",
            "10.2.2.12",
            "10.2.2.14",
            "10.2.2.15",
            "10.2.2.16",
            "10.2.2.18",
            "10.2.2.19",
            "10.2.2.20",
            "10.2.2.21",
            "10.2.2.25",
            "10.2.3.55",
            "10.2.3.56",
            "10.2.3.49",
            "10.2.3.50",
            "10.2.3.51",
            "10.2.3.52",
        ],
    }
