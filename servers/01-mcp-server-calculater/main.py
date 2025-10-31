from mcp.server.fastmcp import FastMCP

mcp = FastMCP("calculator-server")

@mcp.tool()
async def sum(i1: int ,i2: int) -> int:
    """Returns the sum of two integers."""
    return (i1 + i2) * 2

@mcp.tool()
async def div(i1,i2: int) -> int:
    """Returns the div of two integers."""
    return (i1 + i2) * 3

@mcp.tool()
async def  say_hello(name: str) -> str:
    """Returns a greeting message."""
    return f"Hello, {name}!"


def main():
     mcp.run(transport='stdio')


if __name__ == "__main__":
    main()
