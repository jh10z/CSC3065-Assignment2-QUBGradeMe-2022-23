namespace classifygradeapi
{
    public class Program
    {
        public static void Main(string[] args)
        {
            // Add services to the container.
            var policyName = "_myAllowSpecificOrigins";
            var builder = WebApplication.CreateBuilder(args);

            builder.Services.AddCors(options =>
            {
                options.AddPolicy(name: policyName,
                                  builder =>
                                  {
                                      builder
                                        .WithOrigins("*") // specifying the allowed origin
                                        .AllowAnyHeader(); // allowing any header to be sent
                                  });
            });
            builder.Services.AddControllers();

            var app = builder.Build();

            // Configure the HTTP request pipeline.

            app.UseAuthorization();

            app.MapControllers();

            app.UseCors(policyName);

            app.Run();
        }
    }
}