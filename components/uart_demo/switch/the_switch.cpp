#include "the_switch.h"

namespace esphome {
namespace uart_demo {

void UARTDemoSwitch::write_state(bool state) {
  this->parent_->write_binary(state);
  this->publish_state(state);
}

}  // namespace uart_demo
}  // namespace esphome
