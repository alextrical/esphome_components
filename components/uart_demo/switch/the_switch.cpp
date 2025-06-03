#include "the_switch.h"

namespace esphome {
namespace uart_demo {

void TheSwitch::write_state(bool state) {
  this->publish_state(state);
  this->parent_->set_the_switch(state);
}

}  // namespace uart_demo
}  // namespace esphome
