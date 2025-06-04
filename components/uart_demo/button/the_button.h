#pragma once

#include "esphome/components/button/button.h"
#include "../uart_demo.h"

namespace esphome {
namespace uart_demo {

class TheButton : public button::Button, public Parented<UARTDemo> {
 public:
  TheButton() = default;
  // void dump_config() override;

 protected:
  void press_action() override;
};

}  // namespace uart_demo
}  // namespace esphome
