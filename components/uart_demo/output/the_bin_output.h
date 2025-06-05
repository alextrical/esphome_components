#pragma once

#include "esphome/components/switch/switch.h"
#include "../uart_demo.h"
#include "esphome/components/output/binary_output.h"

namespace esphome {
  namespace uart_demo {

    class UARTDemoBOutput : public output::BinaryOutput, public Parented<UARTDemo> {
    public:
      void dump_config(); //override;
      void set_parent(UARTDemo *parent) { this->parent_ = parent; }
    protected:
      void write_state(bool state) override;
      UARTDemo *parent_;
    };

  }  // namespace uart_demo
}  // namespace esphome
