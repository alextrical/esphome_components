#include "the_button.h"

namespace esphome {
  namespace uart_demo {

    void UARTDemoButton::dump_config() {
      // LOG_BUTTON("", "UART Demo Button", this); //fixme
    }

    void UARTDemoButton::press_action() {
      this->parent_->ping();
    }

  }  // namespace uart_demo
}  // namespace esphome
