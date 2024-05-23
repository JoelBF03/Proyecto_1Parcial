<?php

namespace Tests\Feature;

use App\Models\User;
use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class RegisterClientTest extends TestCase
{
    use RefreshDatabase;
    /** @test */
    public function authenticated_user_can_register_client()
    {
        $user = User::factory()->create();
        $response = $this->actingAs($user, 'sanctum')->postJson('/api/cliente', [
            'nombre' => 'Cliente 1',
            'apellido' => 'Apellido 1',
            'email' => 'juan@gmail.com',
            'telefono' => '1234567890',
        ]);
        $response->assertStatus(201);
        $response->assertJsonStructure([
            'id_cliente',
            'nombre',
            'apellido',
            'email',
            'telefono',
            'created_at',
            'updated_at',
        ]);
    }
}
