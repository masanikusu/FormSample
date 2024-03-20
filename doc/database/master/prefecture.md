# 都道府県マスタ

#### 物理名: m_prefecture

|項目名|物理名|データ型|主キー|インデックス|外部キー参照|NULL許可|備考|
|:--:|:--:|:--:|:--:|:--:|:--:|:--:|:--:|
|都道府県コード|prefecture_cd|数値|○|-|-|-||
|都道府県名称|prefecture_name|文字型|-|-|-|-||
|適用開始日時|start_at|タイムスタンプ|-|-|-|-|default:"2000-01-01 00:00:00"|
|適用終了日時|end_at|タイムスタンプ|-|-|-|-|default:"2999-12-31 23:59:59"|
|論理削除フラグ|is_delete|真偽値|-|-|-|-|true:削除データ default:false|
|作成者|create_user|数値|-|-|ユーザーマスタ.ユーザーID|○||
|作成日時|create_at|タイムスタンプ|-|-|-|-||
|更新者|update_user|数値|-|-|ユーザーマスタ.ユーザーID|○||
|更新日時|update_at|タイムスタンプ|-|-|-|-||

##### マスタデータ
|都道府県コード|都道府県名称|
|:--:|:--:|
01|北海道|
02|青森県|
03|岩手県|
04|宮城県|
05|秋田県|
06|山形県|
07|福島県|
08|茨城県|
09|栃木県|
10|群馬県|
11|埼玉県|
12|千葉県|
13|東京都|
14|神奈川県|
15|新潟県|
16|富山県|
17|石川県|
18|福井県|
19|山梨県|
20|長野県|
21|岐阜県|
22|静岡県|
23|愛知県|
24|三重県|
25|滋賀県|
26|京都府|
27|大阪府|
28|兵庫県|
29|奈良県|
30|和歌山県|
31|鳥取県|
32|島根県|
33|岡山県|
34|広島県|
35|山口県|
36|徳島県|
37|香川県|
38|愛媛県|
39|高知県|
40|福岡県|
41|佐賀県|
42|長崎県|
43|熊本県|
44|大分県|
45|宮崎県|
46|鹿児島県|
47|沖縄県|