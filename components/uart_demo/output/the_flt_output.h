#pragma once

#include "esphome/components/switch/switch.h"
#include "../uart_demo.h"
#include "esphome/components/output/float_output.h"

namespace esphome {
  namespace uart_demo {

    class UARTDemoFOutput : public output::FloatOutput, public Parented<UARTDemo> {
    public:
      void dump_config(); //override;
      void set_parent(UARTDemo *parent) { this->parent_ = parent; }
    protected:
      void write_state(float state) override;
      UARTDemo *parent_;
    };

  }  // namespace uart_demo
}  // namespace esphome
