#include <tunables/global>

profile docker-default-custom flags=(attach_disconnected,mediate_deleted) {
  #include <abstractions/base>
  network,
  capability,
  file,
  
  # Deny write & execute access to sensitive paths
  deny /etc/** w,
  deny /var/** w,
  deny /usr/** w,
  deny /proc/sys/** w,
}
