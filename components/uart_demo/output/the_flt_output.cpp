#include "the_flt_output.h"

namespace esphome {
  namespace uart_demo {

    void UARTDemoFOutput::dump_config() {
      // LOG_FLOAT_OUTPUT(this);
    }

    void UARTDemoFOutput::write_state(float state) {
      this->parent_->write_float(state);
    }

  }  // namespace uart_demo
}  // namespace esphome
