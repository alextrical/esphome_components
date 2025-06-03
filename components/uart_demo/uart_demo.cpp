#include "esphome/core/log.h"
#include "uart_demo.h"

namespace esphome {
namespace uart_demo {

static const char *TAG = "uart_demo.component";

void UARTDemo::setup() {

}

void UARTDemo::loop() {

}

void UARTDemo::dump_config(){
  ESP_LOGCONFIG(TAG, "UART Demo Component");
}

void UARTDemo::set_the_switch(bool enable) {
    
}

}  // namespace uart_demo
}  // namespace esphome