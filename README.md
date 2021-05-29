<p align="center">
  <a href="#!">
    <img alt="MOCP logo" src="https://i.ibb.co/y8pDbw6/mocp.png" width="100" />
  </a>
</p>

## Music on Console Player - Discord RPC

> 🎶 why settle for only spotify?

<p align="center">
    <img alt="MOCP RPC Demo" src="https://i.ibb.co/5YqTnx9/demo.png" />
</p>

---

### known bugs / future ?

- [pypresence](https://github.com/qwertyquerty/pypresence/) only allows updating the `Presence` object every 15 seconds. Therefore, showing a time elapsed for the current song in the RPC makes no sense.

- closing / reloading the discord app while the script runs will lead to a asyncio `ConnectionRefusedError`. I'll try to make it such that it waits for the app to reload and then runs itself again or exit gracefully on closing of the discord app.

- I might package it into a pip project and run it / watch for the moc server when the user calls a command.

### why ?

why not. ~~i use mocp sometimes and thought it'd be cool to have rpc for it~~

### the code is bad

I know. If you really hate it that bad, just create an Issue or Pull Request.

### license

[MIT](./LICENSE)

---
