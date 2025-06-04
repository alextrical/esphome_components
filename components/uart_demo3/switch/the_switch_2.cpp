#include "the_switch_2.h"

namespace esphome {
namespace uart_demo {

void TheSwitch2::write_state(bool state) {
  this->publish_state(state);
  this->parent_->set_the_switch_2(state);
}

}  // namespace uart_demo
}  // namespace esphome
