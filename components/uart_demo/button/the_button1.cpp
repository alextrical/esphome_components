#include "the_button1.h"

namespace esphome {
namespace uart_demo {

void TheButton1::press_action() { this->parent_->set_the_button1(); }

}  // namespace uart_demo
}  // namespace esphome
