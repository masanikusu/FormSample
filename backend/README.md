# Environment Setting


### Poetryプロジェクトを作成する
``` sh
$ poetry init
```

### Poetryプロジェクトにライブラリを追加する
```sh
$ poetry add <package_name>
```

### poetry updateコマンドでアップグレードする
```sh
$ poetry update <package_name>
```

### pyproject.tomlを直接編集してアップグレードする
```sh
$ poetry lock
$ poetry install
```

### プロジェクトに指定されたライブラリをインストールする
```sh
$ poetry install
```

### 依存環境解決
``` sh
$ poetry env info
```

### 追加したパッケージ一覧を表示
```sh
$ poetry show
```