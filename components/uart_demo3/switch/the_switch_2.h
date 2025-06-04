#pragma once

#include "esphome/components/switch/switch.h"
#include "../uart_demo.h"

namespace esphome {
namespace uart_demo {

class TheSwitch2 : public switch_::Switch, public Parented<UARTDemo> {
 protected:
  void write_state(bool state) override;
};

}  // namespace uart_demo
}  // namespace esphome
