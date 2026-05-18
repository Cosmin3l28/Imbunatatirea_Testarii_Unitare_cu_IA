import random
from collections.abc import Sequence # type: ignore # mutmut generated
from typing import Annotated # type: ignore # mutmut generated
from typing import Callable # type: ignore # mutmut generated
from typing import ClassVar # type: ignore # mutmut generated
from typing import TypeVar # type: ignore # mutmut generated

TReturn = TypeVar('TReturn') # type: ignore # mutmut generated
MutantDict = Annotated[dict[str, Callable[..., TReturn]], "Mutant"] # type: ignore # mutmut generated


def _mutmut_trampoline(orig: Callable[..., TReturn], mutants: MutantDict, call_args: Sequence, call_kwargs: dict, self_arg = None) -> TReturn: # type: ignore # mutmut generated
    """Forward call to original or mutated function, depending on the environment""" # type: ignore # mutmut generated
    import os # type: ignore # mutmut generated
    mutant_under_test = os.environ.get('MUTANT_UNDER_TEST', '') # type: ignore # mutmut generated
    if not mutant_under_test: # type: ignore # mutmut generated
        # No mutant being tested - call original function
        if self_arg is not None and not hasattr(orig, '__self__'): # type: ignore # mutmut generated
            return orig(self_arg, *call_args, **call_kwargs) # type: ignore # mutmut generated
        else: # type: ignore # mutmut generated
            return orig(*call_args, **call_kwargs) # type: ignore # mutmut generated
    if mutant_under_test == 'fail': # type: ignore # mutmut generated
        from mutmut.__main__ import MutmutProgrammaticFailException # type: ignore # mutmut generated
        raise MutmutProgrammaticFailException('Failed programmatically') # type: ignore # mutmut generated
    elif mutant_under_test == 'stats': # type: ignore # mutmut generated
        from mutmut.__main__ import record_trampoline_hit # type: ignore # mutmut generated
        record_trampoline_hit(orig.__module__ + '.' + orig.__name__) # type: ignore # mutmut generated
        # Check if orig is a bound method (has __self__) or plain function
        if self_arg is not None and not hasattr(orig, '__self__'): # type: ignore # mutmut generated
            result = orig(self_arg, *call_args, **call_kwargs) # type: ignore # mutmut generated
        else: # type: ignore # mutmut generated
            result = orig(*call_args, **call_kwargs) # type: ignore # mutmut generated
        return result # type: ignore # mutmut generated
    prefix = orig.__module__ + '.' + orig.__name__ + '__mutmut_' # type: ignore # mutmut generated
    if not mutant_under_test.startswith(prefix): # type: ignore # mutmut generated
        # Check if orig is a bound method (has __self__) or plain function
        if self_arg is not None and not hasattr(orig, '__self__'): # type: ignore # mutmut generated
            result = orig(self_arg, *call_args, **call_kwargs) # type: ignore # mutmut generated
        else: # type: ignore # mutmut generated
            result = orig(*call_args, **call_kwargs) # type: ignore # mutmut generated
        return result # type: ignore # mutmut generated
    mutant_name = mutant_under_test.rpartition('.')[-1] # type: ignore # mutmut generated
    if self_arg is not None: # type: ignore # mutmut generated
        # call to a class method where self is not bound
        result = mutants[mutant_name](self_arg, *call_args, **call_kwargs) # type: ignore # mutmut generated
    else: # type: ignore # mutmut generated
        result = mutants[mutant_name](*call_args, **call_kwargs) # type: ignore # mutmut generated
    return result # type: ignore # mutmut generated

def luhn_digit(n):
    args = [n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_luhn_digit__mutmut_orig, x_luhn_digit__mutmut_mutants, args, kwargs, None)# type: ignore

def x_luhn_digit__mutmut_orig(n):
    n = 2 * n
    if n > 9:
        return n - 9
    else:
        return n

def x_luhn_digit__mutmut_1(n):
    n = None
    if n > 9:
        return n - 9
    else:
        return n

def x_luhn_digit__mutmut_2(n):
    n = 2 / n
    if n > 9:
        return n - 9
    else:
        return n

def x_luhn_digit__mutmut_3(n):
    n = 3 * n
    if n > 9:
        return n - 9
    else:
        return n

def x_luhn_digit__mutmut_4(n):
    n = 2 * n
    if n >= 9:
        return n - 9
    else:
        return n

def x_luhn_digit__mutmut_5(n):
    n = 2 * n
    if n > 10:
        return n - 9
    else:
        return n

def x_luhn_digit__mutmut_6(n):
    n = 2 * n
    if n > 9:
        return n + 9
    else:
        return n

def x_luhn_digit__mutmut_7(n):
    n = 2 * n
    if n > 9:
        return n - 10
    else:
        return n

x_luhn_digit__mutmut_mutants : MutantDict = { # type: ignore # mutmut generated
    'x_luhn_digit__mutmut_1': x_luhn_digit__mutmut_1, # type: ignore # mutmut generated
    'x_luhn_digit__mutmut_2': x_luhn_digit__mutmut_2, # type: ignore # mutmut generated
    'x_luhn_digit__mutmut_3': x_luhn_digit__mutmut_3, # type: ignore # mutmut generated
    'x_luhn_digit__mutmut_4': x_luhn_digit__mutmut_4, # type: ignore # mutmut generated
    'x_luhn_digit__mutmut_5': x_luhn_digit__mutmut_5, # type: ignore # mutmut generated
    'x_luhn_digit__mutmut_6': x_luhn_digit__mutmut_6, # type: ignore # mutmut generated
    'x_luhn_digit__mutmut_7': x_luhn_digit__mutmut_7 # type: ignore # mutmut generated
} # type: ignore # mutmut generated

x_luhn_digit__mutmut_orig.__name__ = 'x_luhn_digit' # type: ignore # mutmut generated

def luhn_checksum(n):
    args = [n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_luhn_checksum__mutmut_orig, x_luhn_checksum__mutmut_mutants, args, kwargs, None)# type: ignore

def x_luhn_checksum__mutmut_orig(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_1(n):
    l = None
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_2(n):
    l = len(n)
    total_sum = None
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_3(n):
    l = len(n)
    total_sum = 1
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_4(n):
    l = len(n)
    total_sum = 0
    if l / 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_5(n):
    l = len(n)
    total_sum = 0
    if l % 3 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_6(n):
    l = len(n)
    total_sum = 0
    if l % 2 != 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_7(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 1:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_8(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(None):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_9(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) / 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_10(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i - 1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_11(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+2) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_12(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 3 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_13(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 != 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_14(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 1:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_15(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum = int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_16(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum -= int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_17(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(None)
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_18(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum = luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_19(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum -= luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_20(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(None)
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_21(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(None))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_22(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(None):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_23(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) / 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_24(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i - 1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_25(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+2) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_26(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 3 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_27(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 != 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_28(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 1:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_29(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum = luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_30(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum -= luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_31(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(None)
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_32(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(None))
            else:
                total_sum += int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_33(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum = int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_34(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum -= int(n[i])
    return total_sum % 10

def x_luhn_checksum__mutmut_35(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(None)
    return total_sum % 10

def x_luhn_checksum__mutmut_36(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum / 10

def x_luhn_checksum__mutmut_37(n):
    l = len(n)
    total_sum = 0
    if l % 2 == 0:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += int(n[i])
            else:
                total_sum += luhn_digit(int(n[i]))
    else:
        for i in range(l):
            if (i+1) % 2 == 0:
                total_sum += luhn_digit(int(n[i]))
            else:
                total_sum += int(n[i])
    return total_sum % 11

x_luhn_checksum__mutmut_mutants : MutantDict = { # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_1': x_luhn_checksum__mutmut_1, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_2': x_luhn_checksum__mutmut_2, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_3': x_luhn_checksum__mutmut_3, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_4': x_luhn_checksum__mutmut_4, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_5': x_luhn_checksum__mutmut_5, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_6': x_luhn_checksum__mutmut_6, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_7': x_luhn_checksum__mutmut_7, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_8': x_luhn_checksum__mutmut_8, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_9': x_luhn_checksum__mutmut_9, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_10': x_luhn_checksum__mutmut_10, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_11': x_luhn_checksum__mutmut_11, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_12': x_luhn_checksum__mutmut_12, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_13': x_luhn_checksum__mutmut_13, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_14': x_luhn_checksum__mutmut_14, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_15': x_luhn_checksum__mutmut_15, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_16': x_luhn_checksum__mutmut_16, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_17': x_luhn_checksum__mutmut_17, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_18': x_luhn_checksum__mutmut_18, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_19': x_luhn_checksum__mutmut_19, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_20': x_luhn_checksum__mutmut_20, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_21': x_luhn_checksum__mutmut_21, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_22': x_luhn_checksum__mutmut_22, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_23': x_luhn_checksum__mutmut_23, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_24': x_luhn_checksum__mutmut_24, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_25': x_luhn_checksum__mutmut_25, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_26': x_luhn_checksum__mutmut_26, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_27': x_luhn_checksum__mutmut_27, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_28': x_luhn_checksum__mutmut_28, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_29': x_luhn_checksum__mutmut_29, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_30': x_luhn_checksum__mutmut_30, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_31': x_luhn_checksum__mutmut_31, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_32': x_luhn_checksum__mutmut_32, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_33': x_luhn_checksum__mutmut_33, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_34': x_luhn_checksum__mutmut_34, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_35': x_luhn_checksum__mutmut_35, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_36': x_luhn_checksum__mutmut_36, # type: ignore # mutmut generated
    'x_luhn_checksum__mutmut_37': x_luhn_checksum__mutmut_37 # type: ignore # mutmut generated
} # type: ignore # mutmut generated

x_luhn_checksum__mutmut_orig.__name__ = 'x_luhn_checksum' # type: ignore # mutmut generated

def is_luhn_valid(n):
    args = [n]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_is_luhn_valid__mutmut_orig, x_is_luhn_valid__mutmut_mutants, args, kwargs, None)# type: ignore

def x_is_luhn_valid__mutmut_orig(n):
    return luhn_checksum(n) == 0

def x_is_luhn_valid__mutmut_1(n):
    return luhn_checksum(None) == 0

def x_is_luhn_valid__mutmut_2(n):
    return luhn_checksum(n) != 0

def x_is_luhn_valid__mutmut_3(n):
    return luhn_checksum(n) == 1

x_is_luhn_valid__mutmut_mutants : MutantDict = { # type: ignore # mutmut generated
    'x_is_luhn_valid__mutmut_1': x_is_luhn_valid__mutmut_1, # type: ignore # mutmut generated
    'x_is_luhn_valid__mutmut_2': x_is_luhn_valid__mutmut_2, # type: ignore # mutmut generated
    'x_is_luhn_valid__mutmut_3': x_is_luhn_valid__mutmut_3 # type: ignore # mutmut generated
} # type: ignore # mutmut generated

x_is_luhn_valid__mutmut_orig.__name__ = 'x_is_luhn_valid' # type: ignore # mutmut generated

def generate(pref, l):
    args = [pref, l]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_generate__mutmut_orig, x_generate__mutmut_mutants, args, kwargs, None)# type: ignore

def x_generate__mutmut_orig(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_1(pref, l):
    nrand = None
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_2(pref, l):
    nrand = l - len(pref) + 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_3(pref, l):
    nrand = l + len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_4(pref, l):
    nrand = l - len(pref) - 2
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_5(pref, l):
    nrand = l - len(pref) - 1
    assert nrand >= 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_6(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 1, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_7(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "XXnrand > 0XX"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_8(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "NRAND > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_9(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = None
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_10(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(None):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_11(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n = str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_12(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n -= str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_13(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(None)
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_14(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(None))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_15(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(11))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_16(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n = "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_17(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n -= "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_18(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "XX0XX"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_19(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = None
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_20(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(None)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_21(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check == 0:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_22(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 1:
        check = 10 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_23(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = None
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_24(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 + check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_25(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 11 - check
    n = n[:-1] + str(check)
    return n

def x_generate__mutmut_26(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = None
    return n

def x_generate__mutmut_27(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] - str(check)
    return n

def x_generate__mutmut_28(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:+1] + str(check)
    return n

def x_generate__mutmut_29(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-2] + str(check)
    return n

def x_generate__mutmut_30(pref, l):
    nrand = l - len(pref) - 1
    assert nrand > 0, "nrand > 0"
    n = pref
    for i in range(nrand):
        n += str(random.randrange(10))
    n += "0"
    check = luhn_checksum(n)
    if check != 0:
        check = 10 - check
    n = n[:-1] + str(None)
    return n

x_generate__mutmut_mutants : MutantDict = { # type: ignore # mutmut generated
    'x_generate__mutmut_1': x_generate__mutmut_1, # type: ignore # mutmut generated
    'x_generate__mutmut_2': x_generate__mutmut_2, # type: ignore # mutmut generated
    'x_generate__mutmut_3': x_generate__mutmut_3, # type: ignore # mutmut generated
    'x_generate__mutmut_4': x_generate__mutmut_4, # type: ignore # mutmut generated
    'x_generate__mutmut_5': x_generate__mutmut_5, # type: ignore # mutmut generated
    'x_generate__mutmut_6': x_generate__mutmut_6, # type: ignore # mutmut generated
    'x_generate__mutmut_7': x_generate__mutmut_7, # type: ignore # mutmut generated
    'x_generate__mutmut_8': x_generate__mutmut_8, # type: ignore # mutmut generated
    'x_generate__mutmut_9': x_generate__mutmut_9, # type: ignore # mutmut generated
    'x_generate__mutmut_10': x_generate__mutmut_10, # type: ignore # mutmut generated
    'x_generate__mutmut_11': x_generate__mutmut_11, # type: ignore # mutmut generated
    'x_generate__mutmut_12': x_generate__mutmut_12, # type: ignore # mutmut generated
    'x_generate__mutmut_13': x_generate__mutmut_13, # type: ignore # mutmut generated
    'x_generate__mutmut_14': x_generate__mutmut_14, # type: ignore # mutmut generated
    'x_generate__mutmut_15': x_generate__mutmut_15, # type: ignore # mutmut generated
    'x_generate__mutmut_16': x_generate__mutmut_16, # type: ignore # mutmut generated
    'x_generate__mutmut_17': x_generate__mutmut_17, # type: ignore # mutmut generated
    'x_generate__mutmut_18': x_generate__mutmut_18, # type: ignore # mutmut generated
    'x_generate__mutmut_19': x_generate__mutmut_19, # type: ignore # mutmut generated
    'x_generate__mutmut_20': x_generate__mutmut_20, # type: ignore # mutmut generated
    'x_generate__mutmut_21': x_generate__mutmut_21, # type: ignore # mutmut generated
    'x_generate__mutmut_22': x_generate__mutmut_22, # type: ignore # mutmut generated
    'x_generate__mutmut_23': x_generate__mutmut_23, # type: ignore # mutmut generated
    'x_generate__mutmut_24': x_generate__mutmut_24, # type: ignore # mutmut generated
    'x_generate__mutmut_25': x_generate__mutmut_25, # type: ignore # mutmut generated
    'x_generate__mutmut_26': x_generate__mutmut_26, # type: ignore # mutmut generated
    'x_generate__mutmut_27': x_generate__mutmut_27, # type: ignore # mutmut generated
    'x_generate__mutmut_28': x_generate__mutmut_28, # type: ignore # mutmut generated
    'x_generate__mutmut_29': x_generate__mutmut_29, # type: ignore # mutmut generated
    'x_generate__mutmut_30': x_generate__mutmut_30 # type: ignore # mutmut generated
} # type: ignore # mutmut generated

x_generate__mutmut_orig.__name__ = 'x_generate' # type: ignore # mutmut generated

def check(pref, l, num):
    args = [pref, l, num]# type: ignore
    kwargs = {}# type: ignore
    return _mutmut_trampoline(x_check__mutmut_orig, x_check__mutmut_mutants, args, kwargs, None)# type: ignore

def x_check__mutmut_orig(pref, l, num):
    if len(num) != l:
        return False
    preflen = len(pref)
    if num[:preflen] != pref:
        return False
    return is_luhn_valid(num)

def x_check__mutmut_1(pref, l, num):
    if len(num) == l:
        return False
    preflen = len(pref)
    if num[:preflen] != pref:
        return False
    return is_luhn_valid(num)

def x_check__mutmut_2(pref, l, num):
    if len(num) != l:
        return True
    preflen = len(pref)
    if num[:preflen] != pref:
        return False
    return is_luhn_valid(num)

def x_check__mutmut_3(pref, l, num):
    if len(num) != l:
        return False
    preflen = None
    if num[:preflen] != pref:
        return False
    return is_luhn_valid(num)

def x_check__mutmut_4(pref, l, num):
    if len(num) != l:
        return False
    preflen = len(pref)
    if num[:preflen] == pref:
        return False
    return is_luhn_valid(num)

def x_check__mutmut_5(pref, l, num):
    if len(num) != l:
        return False
    preflen = len(pref)
    if num[:preflen] != pref:
        return True
    return is_luhn_valid(num)

def x_check__mutmut_6(pref, l, num):
    if len(num) != l:
        return False
    preflen = len(pref)
    if num[:preflen] != pref:
        return False
    return is_luhn_valid(None)

x_check__mutmut_mutants : MutantDict = { # type: ignore # mutmut generated
    'x_check__mutmut_1': x_check__mutmut_1, # type: ignore # mutmut generated
    'x_check__mutmut_2': x_check__mutmut_2, # type: ignore # mutmut generated
    'x_check__mutmut_3': x_check__mutmut_3, # type: ignore # mutmut generated
    'x_check__mutmut_4': x_check__mutmut_4, # type: ignore # mutmut generated
    'x_check__mutmut_5': x_check__mutmut_5, # type: ignore # mutmut generated
    'x_check__mutmut_6': x_check__mutmut_6 # type: ignore # mutmut generated
} # type: ignore # mutmut generated

x_check__mutmut_orig.__name__ = 'x_check' # type: ignore # mutmut generated