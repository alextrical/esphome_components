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

void UARTDemo::set_the_switch_1(bool enable) {
  ESP_LOGCONFIG(TAG, "The Switch 1 is %d", enable);
}

void UARTDemo::set_the_switch_2(bool enable) {
  ESP_LOGCONFIG(TAG, "The Switch 2 is %d", enable);
}

void UARTDemo::set_the_button_1() {
  ESP_LOGCONFIG(TAG, "The Button 1 Pressed");
}

void UARTDemo::set_the_button_2() {
  ESP_LOGCONFIG(TAG, "The Button 2 Pressed");
}

}  // namespace uart_demo
}  // namespace esphome