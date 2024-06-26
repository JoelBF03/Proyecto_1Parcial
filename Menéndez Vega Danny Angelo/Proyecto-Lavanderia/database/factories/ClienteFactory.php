<?php

namespace Database\Factories;

use Illuminate\Database\Eloquent\Factories\Factory;

/**
 * @extends \Illuminate\Database\Eloquent\Factories\Factory<\App\Models\Cliente>
 */
class ClienteFactory extends Factory
{
    /**
     * Define the model's default state.
     *
     * @return array<string, mixed>
     */
    protected $model = \App\Models\Cliente::class;
    public function definition(): array
    {
        return [
            'nombre' => $this->faker->name,
            'apellido' => $this->faker->name,
            'email' => $this->faker->unique()->safeEmail,
            'telefono' => '1234567890'
            ,
        ];
    }
}
