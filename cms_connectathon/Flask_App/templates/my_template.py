def foo(*args,**kwargs):
    print(args, kwargs)
    return(
    {
    'foo':'bar',
    'param' : kwargs['param1']
    }
    )

if __name__ == "__main__":
    print(foo(param1='bar1'))
