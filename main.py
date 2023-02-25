import sys


def get_lagrange_basis_polynomial(p, w):
    def lagrange_basis_polynomial(x):
        result = 1
        for i, x_i in enumerate(x):
            w_i = bool(w & (1 << i))
            result += x_i * w_i + (1 - x_i) * (1 - w_i)
            result %= p

        return result

    return lagrange_basis_polynomial


def get_multilinear_extension(p, l, encoding_values):
    def multilinear_extension(x):
        result = 0
        for w, encoding_value in enumerate(encoding_values):
            F_w = encoding_value
            X_w = get_lagrange_basis_polynomial(p, w)

            result += F_w * X_w(x)
            result %= p

        return result

    return multilinear_extension


def main():
    _, file_path = sys.argv

    with open(file_path, "r") as f:
        p = int(f.readline())
        l = int(f.readline())

        encoding_values = list(map(int, f.readline().split()))

        r = list(map(int, f.readline().split()))

        if 2**l != len(encoding_values):
            print("Invalid number of encoding values")
            return

        if len(r) != l:
            print("Invalid lenght of r vector")
            return

        multilinear_extension = get_multilinear_extension(p, l, encoding_values)

        print(multilinear_extension(r))


if __name__ == "__main__":
    main()
