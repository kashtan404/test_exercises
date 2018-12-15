## Description <h2> tag

Role Variables
--------------

| Name                                    | Default                       | Description                                   |
|:----------------------------------------|:------------------------------|:----------------------------------------------|
| rsyslog_repeated_msg_reduction          | "on"                          | Enable/disable repeated msg redution          |
| rsyslog_action_file_default_template    | RSYSLOG_TraditionalFileFormat | Action file default template                  |
| rsyslog_klog_permit_non_kernel_facility | "on"                          | Enable/disable logging of non kernel facility |
| rsyslog_udp_enable                      | false                         | Enable or disable rsyslog to listen on UDP    |
| rsyslog_udp_address                     | 127.0.0.1                     | Address to bind to for UDP                    |
| rsyslog_udp_port                        | 514                           | UDP port                                      |
| rsyslog_tcp_enable                      | false                         | Enable or disable rsyslog to listen on TCP    |
| rsyslog_tcp_port                        | 514                           | TCP port                                      |
| rsyslog_apps                            | []                            | List of hashes for app specific configs       |


Example Playbook
----------------

Install rsyslog and configure default logging
```
- hosts: all
  roles:
    - rsyslog
```

Install rsyslog and configure delivering to external syslog server
```
- hosts: all
  vars:
    rsyslog_udp_address: 105.12.23.18
    rsyslog_udp_port: 514
  roles:
    - rsyslog
```

Install rsyslog and configure logging options for testapp
```
- hosts: all
  vars:
    rsyslog_apps:
      - name: testapp
        priority: 49
        lines:
          - "local0.* -/var/log/testapp_0.log"
          - "local1.* -/var/log/testapp_1.log"
          - "& ~"
  roles:
    - rsyslog

```


## Execrise 3 <h2> tag
**Syslog configuration**

Configure rsyslog service with the following settings:
- logging of default log files from /var/log/*
- logging of custom log files

**Ansible**

Configuration must be executed using Ansible utilizing concept of Ansible roles. Ansible role should
accept the following parameters:
- logging only default log files
- logging custom files
- selecting external log server to send logs to

Example of expected result:
- proper contents of /etc/rsyslog.d/ folder
- logs properly delivered to external syslog server