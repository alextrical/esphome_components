#include "the_switch_1.h"

namespace esphome {
namespace uart_demo {

void TheSwitch1::write_state(bool state) {
  this->publish_state(state);
  this->parent_->set_the_switch_1(state);
}

}  // namespace uart_demo
}  // namespace esphome
