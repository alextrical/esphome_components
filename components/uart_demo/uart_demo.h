#pragma once

#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"

namespace esphome {
namespace uart_demo {

class UARTDemo : public uart::UARTDevice, public Component {
  public:
    void setup() override;
    void loop() override;
    void dump_config() override;
    void set_the_switch_1(bool enable);
    void set_the_switch_2(bool enable);
    void set_the_button_1();
    void set_the_button_2();
};


}  // namespace uart_demo
}  // namespace esphome