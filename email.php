<?php

require_once './vendor/autoload.php';

$transport = (new Swift_SmtpTransport('smtp.gmail.com', 465, 'ssl'))
    ->setUsername('emaillll@gmail.com') # enter email address here
    ->setPassword('password') # enter email address password here
;

$mailer = new Swift_Mailer($transport);

$message = (new Swift_Message('Filmai.in #' . date('Y-m-d H:i:s')))
    ->setFrom(['emaillll@gmail.com']) # enter email address here
    ->setTo(['programeriss@gmail.com']) # enter email address here
    ->setBody('Photo of today results!')
;

$attachment = new Swift_Attachment(file_get_contents('page_source.png' ), 'page_source.png', 'image/png');
$message->attach($attachment);

$result = $mailer->send($message);
