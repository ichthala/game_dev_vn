String name;
float value;
int count;

value = 1001.75;
count = 3;

function total_value() {
  count * value;
}

function sell() {
  count = count - 1;
}

while (total_value() > 10) {
  sell();
}
