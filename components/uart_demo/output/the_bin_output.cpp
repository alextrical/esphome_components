#include "the_bin_output.h"

namespace esphome {
  namespace uart_demo {

    void UARTDemoBOutput::dump_config() {
      // LOG_BINARY_OUTPUT(this);
    }

    void UARTDemoBOutput::write_state(bool state) {
      this->parent_->write_binary(state);
    }

  }  // namespace uart_demo
}  // namespace esphome
