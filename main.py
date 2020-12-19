import math


class Converter:

    def convert(self, numbers, format):
        """ Input either a binary or decimal number and
        select the conversion process"""
        converter = self._get_converter(format)
        return converter(numbers)

    def _get_converter(self, format):
        if format == 'Decimal':
            return self._convert_to_decimal
        elif format == 'Binary':
            return self._convert_to_binary
        else:
            raise ValueError(format)

    def _convert_to_decimal(self, numbers):
        decimal = 0
        exponent = 0
        # Iterates throught the string given by the user from the last index
        for digit in numbers[::-1]:
            decimal += int(digit) * math.pow(2, exponent)
            exponent += 1
        return "{:.0f}".format(decimal)

    def _convert_to_binary(self, numbers):
        binary = []
        num = int(numbers)
        while num > 0:
            # Takes the remainder and appends it to the binary list
            remainder = num % 2
            num //= 2
            binary.append(str(remainder))
        binary.reverse()
        return "".join(binary)


if __name__ == "__main__":
    user_conversion_type = input("'Binary'|'Decimal'\nEnter the format you"
                                 " want to convert to:\n>>> ")
    if user_conversion_type == 'Decimal':
        user_number = input("Please enter a Binary number\n>>> ")
    else:
        user_number = input("Please enter a Decimal number\n>>> ")
    user_convert = Converter()
    print(user_convert.convert(user_number, user_conversion_type))