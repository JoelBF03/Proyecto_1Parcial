<?php

namespace App\Console\Commands;

use Illuminate\Console\Command;

class UserDefault extends Command
{
    /**
     * The name and signature of the console command.
     *
     * @var string
     */
    protected $signature = 'app:user-default';

    /**
     * The console command description.
     *
     * @var string
     */
    protected $description = 'Crear usuario por defecto en la base de datos.';

    /**
     * Execute the console command.
     */
    public function handle()
    {
        $this->info('Creando usuario por defecto...');
            $user = new \App\Models\User();
            $user->name = 'Admin';
            $user->email = 'lavanderia@gmail.com';
            $user->password = bcrypt('admin');
            $user->save();
        $this->info('Usuario creado con éxito.');
    }
}
