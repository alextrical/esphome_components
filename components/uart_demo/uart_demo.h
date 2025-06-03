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
    void set_the_switch(bool enable);
    void set_the_button();
};


}  // namespace uart_demo
}  // namespace esphome