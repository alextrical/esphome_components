#include "the_button_1.h"

namespace esphome {
namespace uart_demo {

void TheButton1::press_action() { this->parent_->set_the_button_1(); }

}  // namespace uart_demo
}  // namespace esphome
