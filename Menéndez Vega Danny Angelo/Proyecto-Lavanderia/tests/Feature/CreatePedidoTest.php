<?php

namespace Tests\Feature;

use Illuminate\Foundation\Testing\RefreshDatabase;
use Illuminate\Foundation\Testing\WithFaker;
use Tests\TestCase;

class CreatePedidoTest extends TestCase
{
    use RefreshDatabase;
    /**
     * A basic feature test example.
     */
    /** @test */
    public function it_creates_a_new_order()
    {
        $user = \App\Models\User::factory()->create();
        $this->actingAs($user, 'sanctum');
        $cliente = \App\Models\Cliente::factory()->create();
        $metodoPago = \App\Models\MetodoPago::factory()->create();
        $tipoServicio1 = \App\Models\TipoServicio::factory()->create();
        $tipoServicio2 = \App\Models\TipoServicio::factory()->create();

        $payload = [
            'id_cliente' => $cliente->id_cliente,
            'id_metodo_pago' => $metodoPago->id_metodo_pago,
            'cantidad_pedido' => 100,
            'observacion' => 'Observación de prueba',
            'array_servicios' => [
                [
                    'id_tipo_servicio' => $tipoServicio1->id_tipo_servicio,
                    'cantidad_servicio' => 10,
                    'descripcion' => 'Servicio 1 descripción',
                ],
                [
                    'id_tipo_servicio' => $tipoServicio2->id_tipo_servicio,
                    'cantidad_servicio' => 20,
                    'descripcion' => 'Servicio 2 descripción',
                ]
            ],
            'fecha_pedido' => now()->toDateString(),
            'descripcion' => 'Pedido de prueba',
        ];

        $response = $this->postJson('/api/pedido', $payload);

        $response->assertStatus(200);
        $response->assertJsonStructure([
            'id_pedido',
            'id_cliente',
            'id_metodo_pago',
            'cantidad_pedido',
            'observacion',
            'fecha_pedido',
            'created_at',
            'updated_at',
        ]);

        $this->assertDatabaseHas('pedidos', [
            'id_cliente' => $cliente->id_cliente,
            'id_metodo_pago' => $metodoPago->id_metodo_pago,
            'cantidad_pedido' => 100,
            'fecha_pedido' => now()->toDateString(),
            'observacion' => 'Observación de prueba',
        ]);

        $this->assertDatabaseHas('pedido_servicio', [
            'id_tipo_servicio' => $tipoServicio1->id_tipo_servicio,
            'cantidad_servicio' => 10,
            'descripcion' => 'Servicio 1 descripción'
        ]);

        $this->assertDatabaseHas('pedido_servicio', [
            'id_tipo_servicio' => $tipoServicio2->id_tipo_servicio,
            'cantidad_servicio' => 20,
            'descripcion' => 'Servicio 2 descripción',
        ]);
    }
}
