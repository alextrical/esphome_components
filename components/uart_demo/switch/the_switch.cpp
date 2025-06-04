#include "the_switch.h"

namespace esphome {
namespace uart_demo {

void UARTDemoSwitch::dump_config() {
  // LOG_BUTTON("", "UART Demo Switch", this); //fixme
}

void UARTDemoSwitch::write_state(bool state) {
  this->parent_->write_binary(state);
  this->publish_state(state);
}

}  // namespace uart_demo
}  // namespace esphome
