<?php

require_once './vendor/autoload.php';

$transport = (new Swift_SmtpTransport('smtp.gmail.com', 465, 'ssl'))
    ->setUsername('emaillll@gmail.com')
    ->setPassword('password')
;

$mailer = new Swift_Mailer($transport);

$message = (new Swift_Message('Filmai.in #' . date('Y-m-d H:i:s')))
    ->setFrom(['emaillll@gmail.com'])
    ->setTo(['programeriss@gmail.com'])
    ->setBody('Photo of today results!')
;

$attachment = new Swift_Attachment(file_get_contents('page_source.png' ), 'page_source.png', 'image/png');
$message->attach($attachment);

$result = $mailer->send($message);