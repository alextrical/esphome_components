#include "the_button2.h"

namespace esphome {
namespace uart_demo {

void TheButton2::press_action() { this->parent_->set_the_button2(); }

}  // namespace uart_demo
}  // namespace esphome
