#include "the_button.h"

namespace esphome {
namespace uart_demo {

void TheButton::press_action() { this->parent_->set_the_button(); }

}  // namespace uart_demo
}  // namespace esphome
