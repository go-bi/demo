## 前言
以前在写php的身份验证的时候，一般采用md5，对密码hash一下，偶尔也会加个salt，但是目前来说md5，sha1都已经不算安全，今天再写某项目的身份验证时，打算好好看看php的密码hash方案，发现了password_hash这个东西，认真的看了一下其中一些东西，做下总结。

## Password Hashing
在php5.5中，增加了一种新的加密方式，那就是Password Hashing。
其中包含了4个函数：

+ password_hash：对密码进行hash，得到散列值
+ password_verify：对输入的密码进行校验，判断是否正确
+ password_get_info：获取生成的hash值的信息，包括加密算法，相关加密参数等
+ password_needs_rehash：检查一个hash值是否是使用特定算法及选项创建的

以上这些函数需要在 php5.5以上的环境使用，不过好像也有说5.4也可以使用，不过我没有测验过。
今天主要讲一下password_hash 和 password_verify，它们是一对。

## password_hash
password_hash就是对密码进行hash处理的，语法如下：

语法
```
string password_hash ( string $password , integer $algo [, array $options ] )
```

+ password：用户的密码
+ algo：一个用来在散列密码时指示算法的密码算法常量。
+ options：一个包含有选项的关联数组。目前支持两个选项：salt，在散列密码时加的盐，以及cost，其实用来说明算法递归的层数。如果不设置，将使用随机盐值与默认 cost。

返回值 ：返回哈希后的密码， 或者在失败时返回 FALSE。

## algo可选的值
即当前支持的算法有如下：

PASSWORD_DEFAULT

+ 使用使用 bcrypt 算法 (PHP 5.5.0 默认)。 该常量会随着 PHP以后的更新而改变。 所以，使用此常量生成结果的长度将在未来有变化。 因此，数据库里储存结果的列可超过60个字符。

PASSWORD_BCRYPT

+ 使用 CRYPT_BLOWFISH 算法创建哈希。 可与crypt()兼容使用 ，产生的算法标志为“$2y$” 。 产生60 个字符的字符串。

## 支持的选项

+ salt - 手动提供哈希密码的盐值（salt）。省略此值后，password_hash() 会为每个密码哈希自动生成随机的盐值。然而盐值（salt）选项从 PHP 7.0.0 开始被废弃（deprecated）了。 现在最好选择简单的使用默认产生的盐值。
+ cost - 代表算法使用的 cost。省略时，默认值是 10。数值越大，对计算能力要求越高。 默认值是个不错的底线，但也许可以根据自己硬件的情况，加大这个值。

【 栗子】

```
//栗子1

<?php
echo password_hash("test", PASSWORD_DEFAULT);
//输出值为$2y$10$/ZpSqQs4jcOXwKEZI07WzuYo/liepLJQctmzmRrTr0HvrL8TX7gwa
//每次输出结果都不一致
?>

//栗子2，手动设置cost

<?php
$options = [
    'cost' => 12
];
echo password_hash("test", PASSWORD_BCRYPT, $options);
//输出类似$2y$12$EQDFAJUsyM4nzPTI3zOcrOotgz/hc5qroy4EjGvSb4S2CQ776MBRu
?>

//栗子3，手动设置cost和salt值

<?php
$options = [
    'cost' => 11,
    'salt' => mcrypt_create_iv(22, MCRYPT_DEV_URANDOM),//这里用mcrypt_creat_iv来生成salt；
];
echo password_hash("test", PASSWORD_BCRYPT, $options);
?>
```
## password_verify
password_verify用于验证密码是否和hash值匹配
```
boolean password_verify ( string $password , string $hash )
```

+ password：用户的密码
+ hash一个由 password_hash() 创建的散列值

返回值 ：如果密码和哈希匹配则返回 TRUE，否则返回 FALSE 。

```
$hash="$2y$10$.cEaEUnB0RXho.TeeDwlSOE2dO27QfKLNpvTuRC4Tq9FL11LNqLq2";
$result=password_verify("test",$hash);
var_dump($result); //boolean true

$result2=password_verify("testdd",$hash);
var_dump($result2);//boolean false
```
有了这两个函数，在写代码的时候就不需要考虑加盐的问题了，目前来说相对还是比较安全的。
## 两个函数生成和验证原理
一开始没仔细看php文档，发现相同的密码，每次生成的hash值都不同，然而数据库中没有存储额外的salt值，且使用不同加密手段的时候，使用password_verify验证也都可以验证成功，觉得有点小神奇。
后来仔细看了一下文档并查阅了一下相关资料，文档里提到了一句：使用的算法、cost 和盐值作为哈希的一部分返回。所以验证哈希值的所有信息都已经包含在内。 这使 password_verify() 函数验证的时候，不需要额外储存盐值或者算法的信息。恍然大悟！

![](/1.svg)
