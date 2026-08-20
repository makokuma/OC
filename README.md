# 気象場描画ツール

PythonのStreamlitを使用し、Webブラウザ上で日時・変数・表示範囲などを指定して、任意の気象場を描画するツールです。

気象場の描画にはGrADSを使用しています。

## 動作確認環境

以下の環境で動作を確認しています。

* macOS Tahoe 26.5.2
* Windows Subsystem for Linux 2（WSL2）

## 必要なもの

接続元のPCには、次のコマンドが必要です。

* SSH
* curl
* Webブラウザ

接続先のサーバーには、次の実行環境が必要です。

* Python
* Streamlit
* GrADS
* 本ツールが使用する気象データ

## ファイル構成

起動には、以下のファイルを使用します。

```text
oc.sh
client.conf
server.conf
```

設定ファイルのひな型として、以下を用意しています。

```text
client.conf.example
server.conf.example
```

実際のホスト名、ポート番号、アプリケーションのパス、データのパスなどは、各環境に合わせて設定してください。

実際の設定値を記載した `client.conf` と `server.conf` は、GitHubなどの公開リポジトリには登録しないでください。

## 設定ファイル

### client.conf

`client.conf` は、MacやWSLなどの接続元PCに配置します。

主に以下の情報を設定します。

* SSH接続先
* ローカルポート
* SSH接続の維持設定
* SSH ControlMaster用ソケットの保存場所

ひな型をコピーして作成します。

```bash
mkdir -p ~/.config/oc
cp client.conf.example ~/.config/oc/client.conf
```

その後、利用環境に合わせて内容を編集してください。

```bash
vi ~/.config/oc/client.conf
```

### server.conf

`server.conf` は、Streamlitアプリケーションを実行する接続先サーバーに配置します。

主に以下の情報を設定します。

* アプリケーションの配置場所
* Python仮想環境の場所
* ログファイルの保存場所
* 気象データの保存場所
* 選択可能な日付の下限・上限
* 日付入力の初期値

接続先サーバーで、ひな型をコピーして作成します。

```bash
mkdir -p ~/.config/oc
cp server.conf.example ~/.config/oc/server.conf
```

その後、サーバー環境に合わせて内容を編集してください。

```bash
vi ~/.config/oc/server.conf
```

日付の選択範囲は、次の環境変数で設定します。

```bash
OC_DATE_MIN="YYYY-MM-DD"
OC_DATE_MAX="YYYY-MM-DD"
OC_DATE_DEFAULT="YYYY-MM-DD"

export OC_DATE_MIN
export OC_DATE_MAX
export OC_DATE_DEFAULT
```

`OC_DATE_DEFAULT` は、`OC_DATE_MIN` から `OC_DATE_MAX` の範囲内に設定してください。

### 気象データの配置

気象データのルートディレクトリは、`server.conf` の `OC_DATA_ROOT` で指定します。

CTLファイルは、基本的に次のような構成で参照されます。

```text
OC_DATA_ROOT/
└── YYYY/
    ├── fcst_sfc_LL.ctl
    ├── anl_sfc_LL.ctl
    ├── fcst_p_LL.ctl
    └── anl_p_LL.ctl
```

実際に必要なCTLファイルは、描画する変数の設定によって異なります。

## oc.shの配置

`oc.sh` は任意の場所に配置できます。

本READMEでは、以下への配置を推奨します。

```text
~/.config/oc/oc.sh
```

配置例：

```bash
mkdir -p ~/.config/oc
cp oc.sh ~/.config/oc/oc.sh
```

## 起動方法

### macOS・zsh

現在のシェルで一時的に読み込む場合：

```bash
source ~/.config/oc/oc.sh
oc
```

ターミナルを起動するたびに使用できるようにする場合は、`~/.zshrc` に以下を追加します。

```bash
[ -f "$HOME/.config/oc/oc.sh" ] &&
  source "$HOME/.config/oc/oc.sh"
```

設定を反映します。

```bash
source ~/.zshrc
```

その後、以下で起動できます。

```bash
oc
```

### Linux・WSL・bash

現在のシェルで一時的に読み込む場合：

```bash
source ~/.config/oc/oc.sh
oc
```

ターミナルを起動するたびに使用できるようにする場合は、`~/.bashrc` に以下を追加します。

```bash
[ -f "$HOME/.config/oc/oc.sh" ] &&
  source "$HOME/.config/oc/oc.sh"
```

設定を反映します。

```bash
source ~/.bashrc
```

その後、以下で起動できます。

```bash
oc
```

## クリーンシェルでの動作確認

既存のシェル設定に依存せず動作するか確認する場合は、クリーンシェルを使用できます。

### zsh

```bash
zsh -f
source ~/.config/oc/oc.sh
oc
```

### bash

```bash
bash --noprofile --norc
source ~/.config/oc/oc.sh
oc
```

これらは主に動作確認用です。通常利用では、`.zshrc` または `.bashrc` から `oc.sh` を読み込む方法を推奨します。

## コマンド

### 起動

```bash
oc
```

SSHトンネルを作成し、接続先サーバーでStreamlitを起動した後、Webブラウザを開きます。

### 停止

```bash
oc-stop
```

接続元PCで動作しているOC用SSHトンネルを終了します。

### 状態確認

```bash
oc-status
```

SSHトンネルとStreamlitの応答状態を確認します。

### ログ確認

```bash
oc-log
```

接続先サーバーに保存されたStreamlitのログを表示します。

## 使用方法

現在、以下の機能を利用できます。

* 任意の日付・時刻を指定した気象場の描画
* あらかじめ登録された特定事例の描画
* 描画変数の選択
* 地域プリセットによる表示領域の選択
* 南端・北端・西端・東端の緯度経度を直接入力した表示領域の指定
* 風や海面更正気圧などの重ね描画

ブラウザ上で条件を選択し、「描画する」ボタンを押すと、指定した気象場が表示されます。

### 表示領域の手動指定

「自由に選ぶ」タブの「表示領域」で「手動指定」を選ぶと、次の4項目を直接入力できます。

* 南端緯度
* 北端緯度
* 西端経度
* 東端経度

南端緯度は北端緯度より小さく、西端経度は東端経度より小さく設定してください。

## 注意事項

* `client.conf` と `server.conf` には、環境固有のホスト名やパスが含まれます。公開リポジトリには登録しないでください。
* SSHのパスワード、秘密鍵の内容、APIトークンなどは設定ファイルに直接記載しないでください。
* Streamlitは接続先サーバーの `127.0.0.1` で起動し、SSHポートフォワーディングを経由して接続します。
* 使用するローカルポートが他のアプリケーションで使われている場合は、`client.conf` のポート番号を変更してください。
