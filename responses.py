from random import choice, randint

def get_response(user_input: str) -> str:
    lowered = user_input.lower()

    if 'hello?' in lowered:
        return 'hello?...'
    elif 'hello' in lowered:
        return 'Hello there!'
    elif 'how are you' in lowered:
        return 'Good!'
    elif 'bye' in lowered:
        return 'Bye!'

    # SAT Math Formulas
    elif 'quadratic formula' in lowered:
        return 'Quadratic Formula: x = (-b ± sqrt(b^2 - 4ac)) / (2a)'
    elif 'area of a circle' in lowered:
        return 'Area of a Circle: A = pi * r^2'
    elif 'circumference of a circle' in lowered:
        return 'Circumference of a Circle: C = 2 * pi * r'
    elif 'area of a triangle' in lowered:
        return 'Area of a Triangle: A = 1/2 * base * height'
    elif 'pythagorean theorem' in lowered:
        return 'Pythagorean Theorem: a^2 + b^2 = c^2'
    elif 'slope formula' in lowered:
        return 'Slope Formula: m = (y2 - y1) / (x2 - x1)'
    elif 'distance formula' in lowered:
        return 'Distance Formula: d = sqrt((x2 - x1)^2 + (y2 - y1)^2)'
    elif 'area of a rectangle' in lowered:
        return 'Area of a Rectangle: A = length * width'
    elif 'perimeter of a rectangle' in lowered:
        return 'Perimeter of a Rectangle: P = 2 * (length + width)'
    elif 'volume of a cylinder' in lowered:
        return 'Volume of a Cylinder: V = pi * r^2 * h'
    elif 'volume of a rectangular prism' in lowered:
        return 'Volume of a Rectangular Prism: V = length * width * height'
    elif 'surface area of a sphere' in lowered:
        return 'Surface Area of a Sphere: A = 4 * pi * r^2'
    elif 'volume of a sphere' in lowered:
        return 'Volume of a Sphere: V = 4/3 * pi * r^3'
    elif 'area of a trapezoid' in lowered:
        return 'Area of a Trapezoid: A = 1/2 * (b1 + b2) * height'
    elif 'volume of a cone' in lowered:
        return 'Volume of a Cone: V = 1/3 * pi * r^2 * h'
    elif 'area of a parallelogram' in lowered:
        return 'Area of a Parallelogram: A = base * height'
    elif 'perimeter of a triangle' in lowered:
        return 'Perimeter of a Triangle: P = a + b + c'
    elif 'mean' in lowered:
        return 'Mean: Sum of all values / Number of values'
    elif 'median' in lowered:
        return 'Median: Middle value in an ordered list'
    elif 'mode' in lowered:
        return 'Mode: Most frequently occurring value'
    elif 'standard deviation' in lowered:
        return 'Standard Deviation: sqrt(Sum of (x - mean)^2 / Number of values)'

    # Proportions and Percentages
    elif 'proportion' in lowered:
        return 'Proportion: a/b = c/d -> ad = bc'
    elif 'percent' in lowered:
        return 'Percent: Part / Whole * 100%'
    elif 'percent change' in lowered:
        return 'Percent Change: ((New Value - Old Value) / Old Value) * 100%'
    elif 'ratio' in lowered:
        return 'Ratio: a:b or a/b'
    elif 'scale factor' in lowered:
        return 'Scale Factor: New Size / Original Size'

    # Algebra and Geometry
    elif 'simplify' in lowered:
        return 'Simplify: Combine like terms and reduce fractions'
    elif 'absolute value' in lowered:
        return 'Absolute Value: |x| = x if x >= 0, -x if x < 0'
    elif 'factoring' in lowered:
        return 'Factoring: x^2 - 4 = (x - 2)(x + 2)'
    elif 'systems of equations' in lowered:
        return 'Systems of Equations: Solve by substitution or elimination'
    elif 'linear equation' in lowered:
        return 'Linear Equation: y = mx + b'

    # Trigonometry
    elif 'sine' in lowered:
        return 'Sine: sin(theta) = Opposite / Hypotenuse'
    elif 'cosine' in lowered:
        return 'Cosine: cos(theta) = Adjacent / Hypotenuse'
    elif 'tangent' in lowered:
        return 'Tangent: tan(theta) = Opposite / Adjacent'
    elif 'sin' in lowered:
        return 'sin(theta) = Opposite / Hypotenuse'
    elif 'cos' in lowered:
        return 'cos(theta) = Adjacent / Hypotenuse'
    elif 'tan' in lowered:
        return 'tan(theta) = Opposite / Adjacent'
    elif 'pythagorean identity' in lowered:
        return 'Pythagorean Identity: sin^2(theta) + cos^2(theta) = 1'
    elif 'law of sines' in lowered:
        return 'Law of Sines: a / sin(A) = b / sin(B) = c / sin(C)'
    elif 'law of cosines' in lowered:
        return 'Law of Cosines: c^2 = a^2 + b^2 - 2ab * cos(C)'

    # Exponential and Logarithms
    elif 'exponential growth' in lowered:
        return 'Exponential Growth: A = P(1 + r/n)^(nt)'
    elif 'exponential decay' in lowered:
        return 'Exponential Decay: A = P(1 - r/n)^(nt)'
    elif 'logarithm' in lowered:
        return 'Logarithm: log_b(a) = c if b^c = a'
    elif 'logarithm rules' in lowered:
        return 'Logarithm Rules: log_b(xy) = log_b(x) + log_b(y), log_b(x/y) = log_b(x) - log_b(y), log_b(x^k) = k * log_b(x)'

    # Complex Numbers
    elif 'complex number' in lowered:
        return 'Complex Number: z = a + bi'
    elif 'modulus of a complex number' in lowered:
        return 'Modulus of a Complex Number: |z| = sqrt(a^2 + b^2)'
    elif 'conjugate of a complex number' in lowered:
        return 'Conjugate of a Complex Number: z̅ = a - bi'

    return 'Sorry, I don’t have an answer for that.'
