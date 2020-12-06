学习笔记

## 问题记录

- `assignment_01_server.py` 报错：`ConnectionResetError: [Errno 54] Connection reset by peer `

- `Connected by ('127.0.0.1', 53487)`

  `Connected by ('127.0.0.1', 53528)`

  `Connected by ('127.0.0.1', 53492)`

  当我 `Debug` 客户端的时候，没重新 `Debug` 一次就会建立上面一次链接，这样多次建立的链接是否对服务端有影响？

  

## 注意

- `assignment_02.py ` 运行得到的 `json` 文件结果是不符合 `json` 格式的（`onll one  top-level value`）。但作为文件传输的例子还是先凑活着用一下。
- `assignment_01_client.py` `44` 行，已经用了 `utf-8` 来解码，为什么返回结果不是中文。