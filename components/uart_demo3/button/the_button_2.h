#pragma once

#include "esphome/components/button/button.h"
#include "../uart_demo.h"

namespace esphome {
namespace uart_demo {

class TheButton2 : public button::Button, public Parented<UARTDemo> {
 public:
  TheButton2() = default;

 protected:
  void press_action() override;
};

}  // namespace uart_demo
}  // namespace esphome
