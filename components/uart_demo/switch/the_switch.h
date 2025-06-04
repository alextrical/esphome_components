#pragma once

#include "esphome/components/switch/switch.h"
#include "../uart_demo.h"

namespace esphome {
namespace uart_demo {

class UARTDemoSwitch : public switch_::Switch, public Parented<UARTDemo> {
 public:
  void dump_config(); //override;
  void set_parent(UARTDemo *parent) { this->parent_ = parent; }
 protected:
  void write_state(bool state); //override;
  UARTDemo *parent_;
};

}  // namespace uart_demo
}  // namespace esphome
